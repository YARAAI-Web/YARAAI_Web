rule auto_rule_20250727025938_1347 {
  strings:
    $o0 = "dword_460278" wide ascii nocase
    $o1 = "strncnt" wide ascii nocase
    $o2 = "TrailDown1_0" wide ascii nocase
    $o3 = "TargetIp" wide ascii nocase
  condition:
    4 of ($o*)
}