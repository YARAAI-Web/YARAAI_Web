rule auto_rule_20250727033452_5878 {
  strings:
    $o0 = "m128i_i16" wide ascii nocase
    $o1 = "SystemModuleInformation" wide ascii nocase
  condition:
    all of them
}