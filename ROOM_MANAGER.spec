CREATE OR REPLACE PACKAGE DALE_COMMON.ROOM_MANAGER AS

	--**********************************************
	--CONSTANTS
	--**********************************************

	--**********************************************
	--TYPE DECLARATIONS
	--**********************************************
	TYPE ROOM_REC IS RECORD(
		ROOM_ID              NUMBER(38),
		ABBREVIATION           VARCHAR2(10),
		LOCATION_NAME            VARCHAR2(50),
		MAIL_NAME              VARCHAR2(50),
		DESCRIPTION            VARCHAR2(500),
		TYPE_ID                NUMBER(38),
		HOMEROOM_ROOM_ID       NUMBER(38),
		IS_HOMEROOM              VARCHAR2(1),
		IS_PROCESSOR           VARCHAR2(1),
		USER_CODE            VARCHAR2(3),
		OPEN_YEAR              VARCHAR2(4),
		CLOSE_YEAR             VARCHAR2(4),
		LOCATION_ADDRESS_ID    NUMBER(38),
		MAIL_ADDRESS_ID        NUMBER(38),
		LOCAL_PHONE_ID         NUMBER(38),
		TOLL_FREE_PHONE_ID     NUMBER(38),
		FAX_ID                 NUMBER(38),
		EMAIL_ID               NUMBER(38),
		LOCATION_MANAGER_ID      NUMBER(38),
    		UPDATE_USER_ID         NUMBER(38),
		DISPLAY_LINK           VARCHAR2(1),
		LINK_TITLE             VARCHAR2(50),
		SORT_ORDER             NUMBER(38),
		ROOM_TYPE_IMAGE_PATH VARCHAR2(100),
		IMAGE_MAP_TOP          NUMBER(38),
		IMAGE_MAP_BOTTOM       NUMBER(38),
		IMAGE_MAP_LEFT         NUMBER(38),
		IMAGE_MAP_RIGHT        NUMBER(38),
		IMAGE_MAP_ALT_TEXT     VARCHAR2(40),
		BLOCK_SORT_ORDER      NUMBER(38),
		EMERGENCY_PHONE_ID    NUMBER(38));
	TYPE ROOM_CUR IS REF CURSOR RETURN ROOM_REC;

  TYPE ROOM_ID_REC IS RECORD(
		ROOM_ID              NUMBER(38));
	TYPE ROOM_ID_CUR IS REF CURSOR RETURN ROOM_ID_REC;

	TYPE REC_TYPE_PYMT_ACCT_NMBR IS RECORD (
		ROOM_ID			NUMBER(38),
		PAYMENT_ACCT_NUMBER			NUMBER(38));
	TYPE CUR_TYPE_PYMT_ACCT_NMBRS IS REF CURSOR RETURN REC_TYPE_PYMT_ACCT_NMBR;

	TYPE ROOM_NAME_REC	 IS RECORD(
								ROOM_ID 			NUMBER(38),
								NAME 				VARCHAR2(10),
								OPEN_YEAR			VARCHAR2(4),
								CLOSE_YEAR			VARCHAR2(4),
								TYPE_ID				NUMBER(38,0),
								HOMEROOM_ROOM_ID	NUMBER(38,0));
	TYPE ROOM_NAME_CUR IS REF CURSOR RETURN ROOM_NAME_REC;

	--**********************************************
	--PUBLIC METHODS
	--**********************************************
	PROCEDURE GetRoomNames(nameCursor OUT ROOM_NAME_CUR);
	--**********************************************
	PROCEDURE GetRoom(
		roomId IN NUMBER,
		roomCursor OUT ROOM_CUR,
		addressCursor OUT ROOM_BASE.ROOM_MGR.CUR_ADDRESS,
		phoneCursor OUT ROOM_BASE.ROOM_MGR.CUR_PHONE,
		emailCursor OUT ROOM_BASE.ROOM_MGR.CUR_EMAIL);
	--**********************************************
	PROCEDURE GetAllRooms(roomCursor  OUT ROOM_CUR,
													addressCursor OUT ROOM_BASE.ROOM_MGR.CUR_ADDRESS,
													phoneCursor   OUT ROOM_BASE.ROOM_MGR.CUR_PHONE,
													emailCursor   OUT ROOM_BASE.ROOM_MGR.CUR_EMAIL);


	--**********************************************
	PROCEDURE UpdateUsersPrimaryRoom(currentRoomId IN NUMBER,
																		 newRoomId     IN NUMBER,
																		 startYear       IN VARCHAR2);
	--**********************************************
	PROCEDURE GetTypeCPymtAcctNmbrs(
		reinsuranceYear in VARCHAR2,
		roomId IN NUMBER,
    typeCPymtAcctNbrsCursor OUT CUR_TYPE_PYMT_ACCT_NMBRS);
	--**********************************************
	PROCEDURE GetTypeBPymtAcctNmbrs(
		reinsuranceYear in VARCHAR2,
		roomId IN NUMBER,
    typeBPymtAcctNbrsCursor OUT CUR_TYPE_PYMT_ACCT_NMBRS);
	--**********************************************
  PROCEDURE GetTypeARoomID(
    typeBRoomID            IN NUMBER,
		reinsuranceYear in VARCHAR2,
    typeCRoomID OUT NUMBER
  );
	--**********************************************
	PROCEDURE GetRoomTypeACount (
		  reinsuranceYear in VARCHAR2,
			roomID IN NUMBER,
			roomCount OUT NUMBER,
			filterType IN VARCHAR2 DEFAULT NULL,
			filterValue IN VARCHAR2 DEFAULT NULL
	);
	--**********************************************
	PROCEDURE GetRoomTypeBCount (
		  reinsuranceYear in VARCHAR2,
			roomID IN NUMBER,
			roomCount OUT NUMBER,
			filterType IN VARCHAR2 DEFAULT NULL,
			filterValue IN VARCHAR2 DEFAULT NULL
	);
	--**********************************************
	PROCEDURE GetRoomTypeCCount (
		  reinsuranceYear in VARCHAR2,
			roomID IN NUMBER,
			roomCount OUT NUMBER,
			filterType IN VARCHAR2 DEFAULT NULL,
			filterValue IN VARCHAR2 DEFAULT NULL
	);

END ROOM_MANAGER;
/
