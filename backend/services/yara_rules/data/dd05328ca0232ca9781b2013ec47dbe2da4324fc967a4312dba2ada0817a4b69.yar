rule auto_rule_20250727034652_1998 {
  strings:
    $o0 = "main_loop_entrance" wide ascii nocase
    $o1 = "x4028D4" wide ascii nocase
    $o2 = "insb" wide ascii nocase
    $o3 = "strncnt" wide ascii nocase
    $o4 = "TargetIp" wide ascii nocase
  condition:
    4 of ($o*)
}