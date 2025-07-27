rule auto_rule_20250726103733_1229 {
  strings:
    $o0 = "dword_40E5D0" wide ascii nocase
    $o1 = "dword_40EE88" wide ascii nocase
    $o2 = "GetStringTypeW" wide ascii nocase
  condition:
    3 of ($o*)
}