rule auto_rule_20250726182911_7989 {
  strings:
    $o0 = "EnumDateFormatsW" wide ascii nocase
    $o1 = "LockSetForegroundWindow" wide ascii nocase
    $o2 = "GetSystemTime" wide ascii nocase
    $o3 = "lpFileTime1" wide ascii nocase
  condition:
    4 of ($o*)
}