rule auto_rule_20250727033803_8248 {
  strings:
    $o0 = "bErase" wide ascii nocase
    $o1 = "ulOptions" wide ascii nocase
    $o2 = "PatBlt" wide ascii nocase
    $o3 = "lpcbData" wide ascii nocase
    $o4 = "srand" wide ascii nocase
  condition:
    5 of ($o*)
}