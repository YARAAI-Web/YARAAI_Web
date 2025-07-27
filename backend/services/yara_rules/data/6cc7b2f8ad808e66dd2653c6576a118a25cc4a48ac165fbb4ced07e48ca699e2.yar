rule auto_rule_20250726121151_1113 {
  strings:
    $o0 = "GdipAlloc" wide ascii nocase
    $o1 = "dword_41A020" wide ascii nocase
    $o2 = "_global_unwind2" wide ascii nocase
  condition:
    3 of ($o*)
}