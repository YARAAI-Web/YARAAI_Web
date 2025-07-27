rule auto_rule_20250726194846_8534 {
  strings:
    $o0 = "StrCmpNIA" wide ascii nocase
    $o1 = "pszValueName" wide ascii nocase
    $o2 = "StrCpyNW" wide ascii nocase
    $o3 = "SendMessageCallbackA" wide ascii nocase
    $o4 = "EnumClipboardFormats" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726194849_2001 {
  strings:
    $o0 = "SendIMEMessageExA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726194854_1343 {
  condition:
    auto_rule_20250726194846_8534 or auto_rule_20250726194849_2001
}