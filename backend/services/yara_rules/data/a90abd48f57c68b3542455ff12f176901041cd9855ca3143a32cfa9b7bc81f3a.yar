rule auto_rule_20250727000854_9187 {
  strings:
    $o0 = "byte_404000" wide ascii nocase
    $o1 = "p_InMemoryOrderModuleList" wide ascii nocase
    $o2 = "byte_403128" wide ascii nocase
  condition:
    3 of ($o*)
}