rule auto_rule_20250726071505_9324 {
  strings:
    $o0 = "dword_44603C" wide ascii nocase
    $o1 = "gu_return" wide ascii nocase
    $o2 = "off_445A30" wide ascii nocase
    $o3 = "CodePagea" wide ascii nocase
  condition:
    4 of ($o*)
}