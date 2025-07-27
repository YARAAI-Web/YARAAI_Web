rule auto_rule_20250726093911_6929 {
  strings:
    $o0 = "lpWindowName" wide ascii nocase
    $o1 = "uIDEnableItem" wide ascii nocase
    $o2 = "dword_420B50" wide ascii nocase
  condition:
    3 of ($o*)
}