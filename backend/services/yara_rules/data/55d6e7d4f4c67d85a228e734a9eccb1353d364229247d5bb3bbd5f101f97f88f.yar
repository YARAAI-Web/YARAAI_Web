rule auto_rule_20250726205638_1591 {
  strings:
    $o0 = "GlobalAddAtomA" wide ascii nocase
    $o1 = "lstrcatA" wide ascii nocase
    $o2 = "RegisterShellHookWindow" wide ascii nocase
    $o3 = "cchFileNameMax" wide ascii nocase
    $o4 = "lpwndpl" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726205641_1658 {
  strings:
    $o0 = "uFiletype" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726205645_7179 {
  condition:
    auto_rule_20250726205638_1591 or auto_rule_20250726205641_1658
}