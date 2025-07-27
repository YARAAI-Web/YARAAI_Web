rule auto_rule_20250727022317_7066 {
  strings:
    $o0 = "xF89C853F" wide ascii nocase
    $o1 = "nAtom" wide ascii nocase
    $o2 = "qword_43382B" wide ascii nocase
    $o3 = "plpala" wide ascii nocase
    $o4 = "x5398" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727022320_3385 {
  strings:
    $o0 = "x1B35u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727022324_8518 {
  condition:
    auto_rule_20250727022317_7066 or auto_rule_20250727022320_3385
}