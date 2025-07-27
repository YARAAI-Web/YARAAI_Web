rule auto_rule_20250726102417_9079 {
  strings:
    $o0 = "_fcloseall" wide ascii nocase
    $o1 = "dword_467ED0" wide ascii nocase
    $o2 = "szUserMessage" wide ascii nocase
    $o3 = "_pFirstBlock" wide ascii nocase
    $o4 = "fields" wide ascii nocase
  condition:
    4 of ($o*)
}