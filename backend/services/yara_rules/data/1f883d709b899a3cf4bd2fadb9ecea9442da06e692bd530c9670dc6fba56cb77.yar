rule auto_rule_20250727042908_1401 {
  strings:
    $o0 = "dword_43B473" wide ascii nocase
    $o1 = "dword_43B148" wide ascii nocase
    $o2 = "x43E88B00" wide ascii nocase
    $o3 = "dword_43B4B7" wide ascii nocase
    $o4 = "dword_43B5CC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727042908_0994 {
  strings:
    $o0 = "dword_43B368" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727042912_3443 {
  condition:
    auto_rule_20250727042908_1401 or auto_rule_20250727042908_0994
}