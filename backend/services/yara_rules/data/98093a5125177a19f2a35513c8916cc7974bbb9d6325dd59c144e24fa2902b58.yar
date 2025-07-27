rule auto_rule_20250726071028_4920 {
  strings:
    $o0 = "byte_44BE9C" wide ascii nocase
    $o1 = "tionAndSpinCount" wide ascii nocase
    $o2 = "byte_44BFB4" wide ascii nocase
    $o3 = "overrun" wide ascii nocase
    $o4 = "main_loop_2" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726071031_8308 {
  strings:
    $o0 = "dword_44BE78" wide ascii nocase
    $o1 = "__from_strstr_to_strchr" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
    $o3 = "dword_44BE84" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726071035_2615 {
  condition:
    auto_rule_20250726071028_4920 or auto_rule_20250726071031_8308
}