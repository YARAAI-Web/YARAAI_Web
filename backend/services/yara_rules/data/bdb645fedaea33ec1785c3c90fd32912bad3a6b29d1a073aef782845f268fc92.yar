rule auto_rule_20250727010633_5549 {
  strings:
    $o0 = "start_byte_3" wide ascii nocase
    $o1 = "tionAndSpinCount" wide ascii nocase
    $o2 = "gu_return" wide ascii nocase
    $o3 = "dword_471D7C" wide ascii nocase
    $o4 = "x7FFF" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250727010636_1840 {
  strings:
    $o0 = "off_4723AC" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727010647_6548 {
  condition:
    auto_rule_20250727010633_5549 or auto_rule_20250727010636_1840
}