rule auto_rule_20250727041901_4967 {
  strings:
    $o0 = "dword_4122F8" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
    $o2 = "ActiveWindow" wide ascii nocase
  condition:
    3 of ($o*)
}