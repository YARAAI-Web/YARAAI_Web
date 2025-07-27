rule auto_rule_20250726235256_3027 {
  strings:
    $o0 = "ShellAboutW" wide ascii nocase
    $o1 = "lpTargetPath" wide ascii nocase
    $o2 = "GetConsoleAliasW" wide ascii nocase
    $o3 = "DragQueryFileAorW" wide ascii nocase
  condition:
    4 of ($o*)
}