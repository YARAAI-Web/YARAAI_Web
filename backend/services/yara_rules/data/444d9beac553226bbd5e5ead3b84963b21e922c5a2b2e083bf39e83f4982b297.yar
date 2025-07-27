rule auto_rule_20250726183114_6357 {
  strings:
    $o0 = "dword_42E71D" wide ascii nocase
    $o1 = "x44ECu" wide ascii nocase
    $o2 = "xF74E16E" wide ascii nocase
    $o3 = "x86C253DE" wide ascii nocase
    $o4 = "x7900000001LL" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726183117_7391 {
  strings:
    $o0 = "xD7Eu" wide ascii nocase
    $o1 = "x5330u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726183119_9489 {
  condition:
    auto_rule_20250726183114_6357 or auto_rule_20250726183117_7391
}