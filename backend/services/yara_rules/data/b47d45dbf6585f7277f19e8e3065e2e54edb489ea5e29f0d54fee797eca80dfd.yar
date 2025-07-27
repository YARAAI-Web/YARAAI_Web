rule auto_rule_20250727022408_5755 {
  strings:
    $o0 = "x176Bu" wide ascii nocase
    $o1 = "dword_42A143" wide ascii nocase
    $o2 = "dword_42A173" wide ascii nocase
    $o3 = "x70941FE7" wide ascii nocase
    $o4 = "dword_42A193" wide ascii nocase
  condition:
    4 of ($o*)
}