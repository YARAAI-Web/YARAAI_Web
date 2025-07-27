rule auto_rule_20250726103937_7430 {
  strings:
    $o0 = "aWmDrawitem" wide ascii nocase
    $o1 = "hTemplateFile" wide ascii nocase
    $o2 = "lpSecurityAttributes" wide ascii nocase
  condition:
    3 of ($o*)
}