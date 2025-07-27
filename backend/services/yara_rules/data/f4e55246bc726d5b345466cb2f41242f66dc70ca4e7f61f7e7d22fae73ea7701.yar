rule auto_rule_20250727034257_2025 {
  strings:
    $o0 = "_global_unwind2" wide ascii nocase
    $o1 = "Addend" wide ascii nocase
    $o2 = "dword_469088" wide ascii nocase
  condition:
    3 of ($o*)
}