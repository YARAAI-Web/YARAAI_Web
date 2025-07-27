rule auto_rule_20250726141256_6919 {
  strings:
    $o0 = "_setenvp" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
    $o2 = "dword_45AA70" wide ascii nocase
  condition:
    3 of ($o*)
}