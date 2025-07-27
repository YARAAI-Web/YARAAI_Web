rule auto_rule_20250726110555_8234 {
  strings:
    $o0 = "v737" wide ascii nocase
    $o1 = "xmm4" wide ascii nocase
    $o2 = "var_148" wide ascii nocase
  condition:
    3 of ($o*)
}