rule auto_rule_20250726180953_3212 {
  strings:
    $o0 = "dword_4275CC" wide ascii nocase
    $o1 = "strncnt" wide ascii nocase
    $o2 = "_shift" wide ascii nocase
    $o3 = "_setenvp" wide ascii nocase
    $o4 = "off_42753C" wide ascii nocase
  condition:
    4 of ($o*)
}