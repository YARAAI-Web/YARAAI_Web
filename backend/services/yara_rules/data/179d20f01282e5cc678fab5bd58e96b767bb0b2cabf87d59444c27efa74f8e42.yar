rule auto_rule_20250727004129_7448 {
  strings:
    $o0 = "dword_456CC8" wide ascii nocase
    $o1 = "off_45681C" wide ascii nocase
    $o2 = "TrailDown2" wide ascii nocase
    $o3 = "GetStringTypeW" wide ascii nocase
  condition:
    4 of ($o*)
}