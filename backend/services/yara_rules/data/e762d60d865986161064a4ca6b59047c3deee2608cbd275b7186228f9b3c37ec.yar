rule auto_rule_20250727011045_5047 {
  strings:
    $o0 = "byte_463B40" wide ascii nocase
    $o1 = "main_loop_0" wide ascii nocase
    $o2 = "off_463404" wide ascii nocase
    $o3 = "Handler" wide ascii nocase
    $o4 = "dword_4638C0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727011048_0406 {
  strings:
    $o0 = "byte_463A21" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727011052_8785 {
  condition:
    auto_rule_20250727011045_5047 or auto_rule_20250727011048_0406
}