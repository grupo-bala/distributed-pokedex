from util.singleton import SingletonMeta
from util.id_handler import id_handler
from network.message import Message
from network.client import client
from network.result import Result
from loguru import logger
import jsonpickle

class Proxy(metaclass=SingletonMeta):
    messages_count = 0

    def do_operation(self, object_reference: str, method_id: str, args: dict) -> dict:
        logger.info(f"Proxy - operação: {object_reference} | {method_id} | {args}")
        Proxy.messages_count += 1

        encoded_args = jsonpickle.encode(args, unpicklable=False)
        packed_msg, msg_id = self.__pack_message(
            object_reference, method_id, encoded_args
        )

        logger.info(f"Proxy - packed message: {packed_msg}")

        client.send_message(packed_msg)

        if Proxy.messages_count % 2 == 0:
            client.send_message(packed_msg)

        timeout_error_count = 0

        while True:
            try:
                reply = client.receive_message()
                unpacked_msg: Message = self.__unpack_message(reply)

                if unpacked_msg.id != msg_id:
                    # logger.error(
                    #     "Proxy - ID da mensagem inválido! Unpacked message id: {unpacked_msg.id}, id esperado: {msg_id}"
                    # )

                    print("Proxy - ID da mensagem inválido! Unpacked message id: {unpacked_msg.id}, id esperado: {msg_id}")

                    continue

                result: Result = Result(**jsonpickle.decode(unpacked_msg.arguments))

                if result.status == "Error":
                    logger.error(f"Proxy - erro na operação: {result.result}")

                    raise Exception(result.result)

                logger.success(
                    f"Proxy - operação realizada com sucesso: {result.result}"
                )

                return jsonpickle.decode(result.result)
            except TimeoutError:
                timeout_error_count += 1

                if timeout_error_count == 5:
                    logger.error("Proxy - timeout na operação: 5 tentativas")

                    raise Exception(
                        "O servidor não está respondendo no momento, tente novamente mais tarde."
                    )

                # logger.error("Proxy - timeout na operação")
                print("Proxy - timeout na operação")

                client.send_message(packed_msg)

    def __pack_message(
        self, object_reference: str, method_id: str, args: str
    ) -> [str, int]:
        msg_id = id_handler.id()
        msg = Message(msg_id, 0, object_reference, method_id, args)

        return [jsonpickle.encode(msg, unpicklable=False), msg_id]

    def __unpack_message(self, reply: bytes) -> Message:
        return Message(**jsonpickle.decode(reply.decode()))


proxy = Proxy()
