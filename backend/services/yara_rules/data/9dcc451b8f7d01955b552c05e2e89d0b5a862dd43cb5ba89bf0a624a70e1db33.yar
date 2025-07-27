rule auto_rule_20250726072055_1389 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "UnwindUp2_0" wide ascii nocase
    $o2 = "xFF000000" wide ascii nocase
    $o3 = "dword_449928" wide ascii nocase
    $o4 = "UnwindUp5_0" wide ascii nocase
  condition:
    5 of ($o*)
}