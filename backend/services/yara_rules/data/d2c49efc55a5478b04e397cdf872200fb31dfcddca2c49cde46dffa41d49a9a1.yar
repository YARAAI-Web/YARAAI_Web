rule auto_rule_20250726214515_2384 {
  strings:
    $o0 = "dodwords" wide ascii nocase
    $o1 = "CPtoLCID" wide ascii nocase
    $o2 = "UnwindUp0_0" wide ascii nocase
    $o3 = "byte_401468" wide ascii nocase
    $o4 = "Install" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726214518_0483 {
  strings:
    $o0 = "SetWindowTextA" wide ascii nocase
    $o1 = "dword_406D08" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726214529_9909 {
  condition:
    auto_rule_20250726214515_2384 or auto_rule_20250726214518_0483
}