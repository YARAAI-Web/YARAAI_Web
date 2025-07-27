rule auto_rule_20250727002434_6801 {
  strings:
    $o0 = "_NormalXern" wide ascii nocase
    $o1 = "off_4081C8" wide ascii nocase
    $o2 = "off_408769" wide ascii nocase
    $o3 = "off_408875" wide ascii nocase
    $o4 = "dword_4087D1" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727002437_2753 {
  strings:
    $o0 = "xDF41139D" wide ascii nocase
    $o1 = "x73C9u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727002441_3644 {
  condition:
    auto_rule_20250727002434_6801 or auto_rule_20250727002437_2753
}