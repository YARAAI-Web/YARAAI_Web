rule auto_rule_20250727033557_6937 {
  strings:
    $o0 = "dword_45CDBC" wide ascii nocase
    $o1 = "szCSDVersion" wide ascii nocase
  condition:
    all of them
}