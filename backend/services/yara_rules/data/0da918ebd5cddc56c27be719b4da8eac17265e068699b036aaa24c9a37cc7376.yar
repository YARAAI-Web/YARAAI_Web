rule auto_rule_20250727004608_1909 {
  strings:
    $o0 = "x2B6Eu" wide ascii nocase
    $o1 = "x8A80" wide ascii nocase
    $o2 = "dword_42C018" wide ascii nocase
    $o3 = "hrgnSrc1" wide ascii nocase
    $o4 = "xFFCD8D1E" wide ascii nocase
  condition:
    4 of ($o*)
}