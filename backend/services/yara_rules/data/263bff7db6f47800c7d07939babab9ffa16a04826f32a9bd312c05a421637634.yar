rule auto_rule_20250726112704_8351 {
  strings:
    $o0 = "_ctrlfp" wide ascii nocase
    $o1 = "dword_4C0938" wide ascii nocase
    $o2 = "exit_0" wide ascii nocase
  condition:
    3 of ($o*)
}