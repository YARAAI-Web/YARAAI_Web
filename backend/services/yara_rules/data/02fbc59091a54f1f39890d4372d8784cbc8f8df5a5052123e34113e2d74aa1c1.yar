rule auto_rule_20250726204902_9361 {
  strings:
    $o0 = "x131" wide ascii nocase
    $o1 = "x5B15Du" wide ascii nocase
    $o2 = "dword_4100C7" wide ascii nocase
    $o3 = "dword_40A378" wide ascii nocase
    $o4 = "x6E27" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726204905_8666 {
  strings:
    $o0 = "dword_40A5B8" wide ascii nocase
    $o1 = "dword_41014B" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726204909_6054 {
  condition:
    auto_rule_20250726204902_9361 or auto_rule_20250726204905_8666
}