rule auto_rule_20250727041650_8286 {
  strings:
    $o0 = "GetThreadSelectorEntry" wide ascii nocase
    $o1 = "lpThreadAttributes" wide ascii nocase
    $o2 = "ReadConsoleOutputA" wide ascii nocase
    $o3 = "GetConsoleAliasesLengthA" wide ascii nocase
  condition:
    4 of ($o*)
}