rule auto_rule_20250726074947_4335 {
  strings:
    $o0 = "dword_44E840" wide ascii nocase
    $o1 = "_SEH_epilog" wide ascii nocase
  condition:
    all of them
}