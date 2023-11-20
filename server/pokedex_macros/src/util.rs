pub fn make_ascii_titlecase(s: &mut str) {
    if let Some(r) = s.get_mut(0..1) {
        r.make_ascii_uppercase();
    }
}

pub fn format_camel_case(s: &str) -> String {
    let mut words: Vec<_> = s.split("_")
        .map(|s| { s.to_string() })
        .collect();

    for mut word in words.iter_mut() {
        make_ascii_titlecase(&mut word);
    }

    words.join("")
}