rule auto_rule_20250726175909_5167 {
  strings:
    $o0 = "dword_4C32E0" wide ascii nocase
    $o1 = "start_6" wide ascii nocase
    $o2 = "off_48ED5C" wide ascii nocase
    $o3 = "aSin" wide ascii nocase
    $o4 = "_ErrorHandling_0" wide ascii nocase
  condition:
    4 of ($o*)
}