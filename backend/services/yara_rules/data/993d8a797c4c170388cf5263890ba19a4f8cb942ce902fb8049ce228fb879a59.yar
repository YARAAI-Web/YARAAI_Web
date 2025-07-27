rule auto_rule_20250726093429_3770 {
  strings:
    $o0 = "GetConsoleAliasesLengthA" wide ascii nocase
    $o1 = "SendNotifyMessageA" wide ascii nocase
    $o2 = "FileTimeToDosDateTime" wide ascii nocase
  condition:
    3 of ($o*)
}