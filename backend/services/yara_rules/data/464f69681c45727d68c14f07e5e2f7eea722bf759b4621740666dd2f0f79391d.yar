rule auto_rule_20250726065200_1776 {
  strings:
    $o0 = "GetStringTypeA" wide ascii nocase
    $o1 = "dword_440144" wide ascii nocase
    $o2 = "copy_start" wide ascii nocase
    $o3 = "TrailDown0_0" wide ascii nocase
    $o4 = "byte_440581" wide ascii nocase
  condition:
    4 of ($o*)
}