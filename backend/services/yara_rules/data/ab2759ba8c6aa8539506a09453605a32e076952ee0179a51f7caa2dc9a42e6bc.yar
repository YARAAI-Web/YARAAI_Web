rule auto_rule_20250727020212_8425 {
  strings:
    $o0 = "lpSecurityAttributes" wide ascii nocase
    $o1 = "aGsyst12111cgcr" wide ascii nocase
    $o2 = "uSize" wide ascii nocase
    $o3 = "flAllocationType" wide ascii nocase
  condition:
    4 of ($o*)
}