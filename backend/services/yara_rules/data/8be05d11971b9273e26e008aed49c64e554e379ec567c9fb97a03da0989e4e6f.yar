rule auto_rule_20250726084804_0132 {
  strings:
    $o0 = "x15CA" wide ascii nocase
    $o1 = "CharUpperA" wide ascii nocase
    $o2 = "lpfnHook" wide ascii nocase
    $o3 = "tagOFNA" wide ascii nocase
    $o4 = "bUnderline" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726084807_9272 {
  strings:
    $o0 = "x2B01" wide ascii nocase
    $o1 = "wVersion" wide ascii nocase
    $o2 = "xF89C85D8" wide ascii nocase
    $o3 = "xF89C853E" wide ascii nocase
    $o4 = "dword_41ABD6" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726084811_0803 {
  strings:
    $o0 = "off_40D68C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726084812_1654 {
  condition:
    (auto_rule_20250726084804_0132 and auto_rule_20250726084807_9272) or (auto_rule_20250726084804_0132 and auto_rule_20250726084811_0803) or (auto_rule_20250726084807_9272 and auto_rule_20250726084811_0803)
}