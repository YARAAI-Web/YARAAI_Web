rule auto_rule_20250726190129_2461 {
  strings:
    $o0 = "uMsg" wide ascii nocase
    $o1 = "GetMenuStringA" wide ascii nocase
    $o2 = "hrgnUpdate" wide ascii nocase
    $o3 = "fInherit" wide ascii nocase
  condition:
    4 of ($o*)
}