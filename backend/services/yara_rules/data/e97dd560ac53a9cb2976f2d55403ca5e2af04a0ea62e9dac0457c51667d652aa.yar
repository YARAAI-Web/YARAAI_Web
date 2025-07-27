rule auto_rule_20250727023733_7974 {
  strings:
    $o0 = "old_esp" wide ascii nocase
    $o1 = "Runtime" wide ascii nocase
    $o2 = "xFF000000" wide ascii nocase
    $o3 = "dword_477234" wide ascii nocase
  condition:
    4 of ($o*)
}