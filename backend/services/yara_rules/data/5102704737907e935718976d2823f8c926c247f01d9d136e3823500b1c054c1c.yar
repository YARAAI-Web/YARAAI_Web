rule auto_rule_20250726103423_2034 {
  strings:
    $o0 = "x2BE1" wide ascii nocase
    $o1 = "x70941FD5" wide ascii nocase
    $o2 = "lstrlenW" wide ascii nocase
    $o3 = "GetPriorityClass" wide ascii nocase
    $o4 = "x83ED" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726103426_8488 {
  strings:
    $o0 = "off_41C65F" wide ascii nocase
    $o1 = "x6E06u" wide ascii nocase
    $o2 = "x4F87" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726103431_4304 {
  condition:
    auto_rule_20250726103423_2034 or auto_rule_20250726103426_8488
}