rule auto_rule_20250726193732_2492 {
  strings:
    $o0 = "GetConsoleAliasExesW" wide ascii nocase
    $o1 = "lpValue" wide ascii nocase
    $o2 = "ExeNameBufferLength" wide ascii nocase
    $o3 = "StrRChrIW" wide ascii nocase
    $o4 = "DuplicateIcon" wide ascii nocase
  condition:
    4 of ($o*)
}