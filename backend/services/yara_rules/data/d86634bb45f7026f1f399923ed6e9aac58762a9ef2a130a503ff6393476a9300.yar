rule auto_rule_20250727031635_9896 {
  strings:
    $o0 = "WinWaitDelay" wide ascii nocase
    $o1 = "script" wide ascii nocase
    $o2 = "dword_4C1324" wide ascii nocase
  condition:
    3 of ($o*)
}