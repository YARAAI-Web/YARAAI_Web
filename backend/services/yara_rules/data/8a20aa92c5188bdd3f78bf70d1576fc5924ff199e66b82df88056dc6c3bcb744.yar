rule auto_rule_20250726121943_6154 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "dword_446BDC" wide ascii nocase
    $o2 = "strcat" wide ascii nocase
    $o3 = "_except_handler3" wide ascii nocase
    $o4 = "_CrtSetDbgFlag" wide ascii nocase
  condition:
    4 of ($o*)
}