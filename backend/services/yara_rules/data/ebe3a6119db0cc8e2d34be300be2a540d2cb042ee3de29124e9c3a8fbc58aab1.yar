rule auto_rule_20250726091211_5876 {
  strings:
    $o0 = "strcspn" wide ascii nocase
    $o1 = "dword_471020" wide ascii nocase
    $o2 = "byte_475FA0" wide ascii nocase
  condition:
    3 of ($o*)
}