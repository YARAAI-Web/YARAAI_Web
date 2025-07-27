rule auto_rule_20250726094842_4634 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "dword_4643DC" wide ascii nocase
    $o2 = "dword_462020" wide ascii nocase
  condition:
    3 of ($o*)
}