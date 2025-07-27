rule auto_rule_20250726235950_9493 {
  strings:
    $o0 = "x2781u" wide ascii nocase
    $o1 = "bStrikeOut" wide ascii nocase
    $o2 = "GetROP2" wide ascii nocase
    $o3 = "dword_42900C" wide ascii nocase
    $o4 = "x8A29A12D" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726235954_3643 {
  strings:
    $o0 = "_GetUserObjectSecurityGetUserObjectSecu" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726235957_6755 {
  condition:
    auto_rule_20250726235950_9493 or auto_rule_20250726235954_3643
}